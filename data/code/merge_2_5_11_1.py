import difflib
from typing import List, Dict
def compare_strings_high_performance(str1: str, str2: str) -> Dict[str, any]:
    sequence_matcher = difflib.SequenceMatcher(None, str1, str2)
    matches = []
    for tag, i1, j1, i2, j2 in sequence_matcher.get_opcodes():
        if tag == 'equal':
            match_dict: Dict[str, any] = {
                "type": "match",
                "start_str_1": i1,
                "end_str_1": j1,
                "start_str_2": i2,
                "end_str_2": j2,
                "value": str1[i1:j1] if len(str1) > 0 else ""
            }
        elif tag == 'replace':
            match_dict: Dict[str, any] = {
                "type": "replacement",
                "start_str_1": i1,
                "end_str_1": j1,
                "start_str_2": i2,
                "end_str_2": j2,
                "value_before": str1[i1:j1] if len(str1) > 0 else "",
                "value_after": str2[i2:j2] if len(str2) > 0 else ""
            }
        elif tag == 'delete':
            match_dict: Dict[str, any] = {
                "type": "deletion",
                "start_str_1": i1,
                "end_str_1": j1,
                "value_before": str1[i1:j1],
                "inserted_value_after": "" if len(str2) == 0 else None
            }
        elif tag == 'insert':
            match_dict: Dict[str, any] = {
                "type": "insertion",
                "start_str_1": i1,
                "end_str_1": j1,
                "value_before": "" if len(str1) == 0 else None,
                "inserted_value_after": str2[i2:j2] if len(str2) > 0 else ""
            }
        matches.append(match_dict)
    similarity_ratio = sequence_matcher.ratio()
    report: Dict[str, any] = {
        "similarity_score": round(similarity_ratio * 100, 4),
        "total_chars_str_1": len(str1),
        "total_chars_str_2": len(str2),
        "operations_count": len(matches),
        "detailed_operations": matches
    }
    return report
if __name__ == '__main__':
    sample_text_a = "The quick brown fox jumps over the lazy dog"
    sample_text_b = "The quick brown fox jumped over the lazy dogs"
    result_json: Dict[str, any] = compare_strings_high_performance(sample_text_a, sample_text_b)
    print(result_json)