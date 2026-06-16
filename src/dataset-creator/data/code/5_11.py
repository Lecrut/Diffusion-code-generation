import difflib
import json
def compare_strings_high_performance(s1: str, s2: str) -> dict:
    sequence_matcher = difflib.SequenceMatcher(None, s1, s2)
    matches = []
    for tag, i1, j1, i2, j2 in sequence_matcher.get_opcodes():
        if tag == 'equal':
            matches.append({'type': 'match', 'start_s1': i1, 'end_s1': j1, 'start_s2': i2, 'end_s2': j2})
        elif tag == 'replace':
            matches.append({'type': 'mismatch', 'start_s1': i1, 'end_s1': j1, 'start_s2': i2, 'end_s2': j2})
    similarity_ratio = sequence_matcher.ratio()
    result = {
        "similarity_score": round(similarity_ratio * 100, 4),
        "operations": matches,
        "string_1_length": len(s1),
        "string_2_length": len(s2)
    }
    return result
if __name__ == '__main__':
    sample_str_a = "Hello World"
    sample_str_b = "Hell o Worl d"
    output_data = compare_strings_high_performance(sample_str_a, sample_str_b)
    print(json.dumps(output_data))