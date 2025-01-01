# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'math.sk'
author = 'Michal Kracalik'

# -- General configuration ---------------------------------------------------
extensions = ["myst_parser", "sphinx_design"]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'
html_static_path = ['_static']

language = "en"
myst_html_meta = {
    "description lang=en": "metadata description",
    "description lang=fr": "description des métadonnées",
    "keywords": "Sphinx, MyST",
    "property=og:locale":  "en_US"
}