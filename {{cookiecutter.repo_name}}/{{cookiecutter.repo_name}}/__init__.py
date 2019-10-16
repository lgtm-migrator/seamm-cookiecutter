# -*- coding: utf-8 -*-

"""
{{cookiecutter.repo_name}}
{{cookiecutter.description}}
"""

# Bring up the classes so that they appear to be directly in
# the {{ cookiecutter.repo_name }} package.

from {{ cookiecutter.repo_name }}.{{ cookiecutter.first_module_name }} import {{ cookiecutter.first_module_name }}  # noqa: F401
from {{ cookiecutter.repo_name }}.{{ cookiecutter.first_module_name }}_parameters import {{ cookiecutter.first_module_name }}Parameters  # noqa: F401
from {{ cookiecutter.repo_name }}.{{ cookiecutter.first_module_name }}_step import {{ cookiecutter.first_module_name }}Step  # noqa: F401
from {{ cookiecutter.repo_name }}.tk_{{ cookiecutter.first_module_name }} import Tk{{ cookiecutter.first_module_name }}  # noqa: F401

# Handle versioneer
from ._version import get_versions
__author__ = """{{ cookiecutter.author_name }}"""
__email__ = '{{ cookiecutter.author_email }}'
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions