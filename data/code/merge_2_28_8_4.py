import re
from collections import Counter
def extract_favorites(logs):
    pattern = r'\b(?:dog|cat|lion|tiger|elephant|bear|monkey|rabbit)\b'
    matches = []
    for log in logs:
        found = re.findall(pattern, log.lower())
        if found:
            matches.extend(found)
    favorites = dict(Counter(matches).most_common(5))
    return favorites
if __name__ == '__main__':
    sample_logs = [
        "The dog barked loudly in the park.",
        "My cat is sleeping on the sofa today.",
        "A lion roared at sunset near the savanna.",
        "I love my pet rabbit and tiger very much.",
        "No animals were mentioned here."
    ]
    result = extract_favorites(sample_logs)
    print(result)