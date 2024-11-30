from playwright.sync_api import sync_playwright


def test_open_homepage():
    with sync_playwright() as p:
        # הפעלת דפדפן
        browser = p.chromium.launch(headless=False)  # כדי לראות את הדפדפן בזמן ריצה
        page = browser.new_page()

        # פתיחת האתר
        page.goto("http://the-internet.herokuapp.com/")

        # בדיקה שהכותרת בדף הבית נכונה
        header = page.locator("h1")
        assert header.text_content() == "Welcome to the-internet", "error: wrong title!"

        print("The page loaded successfully with the right title")

        browser.close()


if __name__ == "__main__":
    test_open_homepage()
