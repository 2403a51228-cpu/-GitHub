from pathlib import Path

def test_website_exists():
    assert Path("site/index.html").exists()

def test_website_content():
    content = Path("site/index.html").read_text()
    assert "Welcome to My Website" in content
