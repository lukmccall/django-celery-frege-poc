import pytest

from fregepoc.repositories.analyzers.base import AnalyzerFactory
from fregepoc.repositories.constants import ProgrammingLanguages
from fregepoc.repositories.factories import RepositoryFileFactory
from fregepoc.repositories.utils.tests import MOCK_DOWNLOAD_PATH


@pytest.mark.django_db
class TestAnalyzers:
    @pytest.mark.parametrize(
        ["lang", "repo_file_params"],
        [
            (ProgrammingLanguages.CPP, {"repo_relative_file_path": "ans.cpp"}),
            (
                ProgrammingLanguages.RUBY,
                {"repo_relative_file_path": "hello_world.rb"},
            ),
            (
                ProgrammingLanguages.JAVA,
                {"repo_relative_file_path": "binary_tree.java"},
            ),
            (
                ProgrammingLanguages.PHP,
                {"repo_relative_file_path": "binary_search.php"},
            ),
            (
                ProgrammingLanguages.PYTHON,
                {"repo_relative_file_path": "hello_world.py"},
            ),
        ],
    )
    def test_analyzers_make_some_analysis(
        self, lang, repo_file_params, settings, dummy_repo
    ):
        settings.DOWNLOAD_PATH = MOCK_DOWNLOAD_PATH
        analyzers = AnalyzerFactory.make_analyzers(lang)
        repo_file = RepositoryFileFactory(
            repository=dummy_repo,
            language=lang,
            **repo_file_params,
        )
        for analyzer in analyzers:
            result_dict = analyzer.analyze(repo_file)
            assert result_dict
