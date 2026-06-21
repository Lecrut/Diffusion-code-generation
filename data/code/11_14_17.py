import collections
import json

def detect_character_frequency_duplicates(text: str) -> dict:
    if not text:
        return {}
    freq_map = collections.Counter(text)
    duplicates = {char: count for char, count in freq_map.items() if count > 1}
    return duplicates

def format_duplicate_report(duplicates: dict) -> str:
    if not duplicates:
        return 'No duplicate characters found.'
    sorted_dups = sorted(duplicates.items(), key=lambda item: item[1], reverse=True)
    lines = [f"'{char}': {count}" for char, count in sorted_dups]
    return ', '.join(lines)
if __name__ == '__main__':
    sample_text = 'abracadabra'
    result = detect_character_frequency_duplicates(sample_text)
    report = format_duplicate_report(result)
    print(f'Duplicate characters: {result}')
    print(f'Report: {report}')
    sample_text_2 = 'hello world'
    result_2 = detect_character_frequency_duplicates(sample_text_2)
    print(f"Duplicate characters in 'hello world': {result_2}")