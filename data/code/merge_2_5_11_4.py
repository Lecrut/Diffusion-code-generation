import difflib
from typing import List, Dict
def compare_strings_high_performance(s1: str, s2: str) -> Dict[str, object]:
    sequence_matcher = difflib.SequenceMatcher(None, s1, s2)
    matches = []
    for tag, i1, j1, i2, j2 in sequence_matcher.get_opcodes():
        if tag == 'equal':
            match_dict: Dict[str, object] = {
                "type": "match",
                "start_s1": int(i1),
                "end_s1": int(j1) + 1,
                "start_s2": int(i2),
                "end_s2": int(j2) + 1,
                "value": s1[i1:j1] if i1 < j1 else ""
            }
        elif tag == 'replace':
            match_dict = {
                "type": "replace",
                "start_s1": int(i1),
                "end_s1": int(j1) + 1,
                "start_s2": int(i2),
                "end_s2": int(j2) + 1,
                "value_before": s1[i1:j1] if i1 < j1 else "",
                "value_after": s2[i2:j2] if i2 < j2 else ""
            }
        elif tag == 'delete':
            match_dict = {
                "type": "delete",
                "start_s1": int(i1),
                "end_s1": int(j1) + 1,
                "value_before": s1[i1:j1] if i1 < j1 else ""
            }
        elif tag == 'insert':
            match_dict = {
                "type": "insert",
                "start_s2": int(i2),
                "end_s2": int(j2) + 1,
                "value_after": s2[i2:j2] if i2 < j2 else ""
            }
        matches.append(match_dict)
    similarity_ratio = sequence_matcher.ratio()
    return {
        "similarity_score": float(similarity_ratio),
        "operations": matches,
        "string_1_length": len(s1),
        "string_2_length": len(s2),
        "common_subsequence_count": sum(1 for tag in sequence_matcher.get_opcodes() if tag == 'equal')
    }
if __name__ == '__main__':
    sample_str_a = "The quick brown fox jumps over the lazy dog"
    sample_str_b = "The quick brown fox jumped over the lazy dogs"
    result_data: Dict[str, object] = compare_strings_high_performance(sample_str_a, sample_str_b)
    import json
    output_json_string: str = json.dumps(result_data, indent=2)
    print(output_json_string)