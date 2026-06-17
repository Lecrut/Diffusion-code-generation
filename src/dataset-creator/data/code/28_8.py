import re
from typing import Dict, List
def extract_animals(text: str) -> List[str]:
    pattern = r'\b(cat|dog|bird|rabbit|elephant|lion|tiger|bear|wolf|horse)\b'
    return re.findall(pattern, text.lower())
def process_logs(log_entries: List[str]) -> Dict[int, str]:
    all_animals = []
    for entry in log_entries:
        found = extract_animals(entry)
        if not found:
            continue
        first_occurrence_index = 0
        count_in_entry = len(found)
        global_counts = {}
        for i, animal in enumerate(all_animals):
            global_counts[animal] = global_counts.get(animal, 0) + (1 if all_animals.count(animal) == found.index(animal) else 0)
    return {"total_entries": len(log_entries), "favorite_count": max(global_counts.values(), default=0)}
if __name__ == '__main__':
    sample_logs = [
        "The cat sat on the mat.",
        "My dog loves to run in the park.",
        "Birds chirp loudly at dawn.",
        "Rabbits hide under bushes."
    ]
    result = process_logs(sample_logs)
    print(result)