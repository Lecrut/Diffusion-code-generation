import re
from collections import Counter
def extract_favorites(logs):
    pattern = r'\b(?:cat|dog|bird|fish|rabbit|hamster)\b'
    matches = [match.group() for match in re.finditer(pattern, logs)]
    return dict(Counter(matches))
if __name__ == '__main__':
    raw_logs = "The cat sat on the mat. My dog is happy. Birds fly high."
    favorites = extract_favorites(raw_logs)
    print(favorites)