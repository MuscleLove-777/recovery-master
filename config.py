"""リカバリーマスター - ブログ固有設定"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "リカバリーマスター"
BLOG_DESCRIPTION = "ストレッチ・リカバリー・怪我予防の専門ブログ"
BLOG_URL = "https://musclelove-777.github.io/recovery-master"
BLOG_LANGUAGE = "ja"
GITHUB_REPO = "MuscleLove-777/recovery-master"

TARGET_CATEGORIES = [
    "ストレッチ実践",
    "筋膜リリース",
    "怪我予防・リハビリ",
    "睡眠・休息",
    "モビリティ・柔軟性",
]

THEME = {
    "primary": "#8b5cf6",
    "accent": "#a78bfa",
    "gradient_start": "#8b5cf6",
    "gradient_end": "#7c3aed",
    "dark_bg": "#0f0a20",
    "dark_surface": "#1a1530",
    "light_bg": "#f5f3ff",
    "light_surface": "#ffffff",
}

MAX_ARTICLE_LENGTH = 2500
ARTICLES_PER_DAY = 2
SCHEDULE_HOURS = [9, 21]

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"

ENABLE_SEO_OPTIMIZATION = True
MIN_SEO_SCORE = 70
MIN_KEYWORD_DENSITY = 1.0
MAX_KEYWORD_DENSITY = 3.0
META_DESCRIPTION_LENGTH = 120
ENABLE_INTERNAL_LINKS = True

AFFILIATE_LINKS = {
    "ストレッチ器具": [
        {"service": "Amazon フォームローラー", "url": "https://www.amazon.co.jp", "description": "筋膜リリース用フォームローラー"},
        {"service": "Amazon ストレッチバンド", "url": "https://www.amazon.co.jp", "description": "ストレッチ用レジスタンスバンド"},
        {"service": "Amazon マッサージガン", "url": "https://www.amazon.co.jp", "description": "筋肉リカバリー用マッサージガン"},
    ],
    "リカバリーグッズ": [
        {"service": "Amazon コンプレッションウェア", "url": "https://www.amazon.co.jp", "description": "リカバリー用コンプレッションウェア"},
        {"service": "Amazon アイシング", "url": "https://www.amazon.co.jp", "description": "アイシング用品"},
    ],
    "睡眠・休息": [
        {"service": "Amazon 枕", "url": "https://www.amazon.co.jp", "description": "睡眠の質を上げる枕"},
        {"service": "Amazon サプリ", "url": "https://www.amazon.co.jp", "description": "リカバリーサプリメント"},
    ],
    "書籍": [
        {"service": "Amazon", "url": "https://www.amazon.co.jp", "description": "ストレッチ・リカバリー書籍"},
        {"service": "楽天ブックス", "url": "https://books.rakuten.co.jp", "description": "柔軟性・モビリティ書籍"},
    ],
}
AFFILIATE_TAG = "musclelove07-22"

ADSENSE_CLIENT_ID = os.environ.get("ADSENSE_CLIENT_ID", "")
DASHBOARD_PORT = 8080

# Google Analytics (GA4)
GOOGLE_ANALYTICS_ID = "G-CSFVD34MKK"

# Google Search Console 認証ファイル
SITE_VERIFICATION_FILES = {
    "googlea31edabcec879415.html": "google-site-verification: googlea31edabcec879415.html",
}
