import re
from collections import Counter
def extract_favorites(log_text):
    pattern = r'\b(cat|dog|bird|fish|rabbit|hamster)\b'
    matches = re.findall(pattern, log_text)
    return dict(Counter(matches))
if __name__ == '__main__':
    raw_logs = "The cat sat on the mat. My dog loves to run. Birds fly high in the sky."
    favorites = extract_favorites(raw_logs)
    print(favorites)