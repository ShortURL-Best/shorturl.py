# Configuration file for the Sphinx documentation builder.

# -- Project information
project = "shorturl.py"
copyright = "2023-Present"
author = "6A-Realm"

release = "p0.0.2"
version = "p0.0.2"

# -- General configuration
extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]

# -- Options for HTML output
html_theme = "sphinx_rtd_theme"
html_show_sphinx = False

# -- Options for EPUB output
epub_show_urls = "footnote"