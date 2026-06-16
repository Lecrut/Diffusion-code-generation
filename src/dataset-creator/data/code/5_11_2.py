import difflib
from typing import List, Dict
def compare_strings_high_performance(s1: str, s2: str) -> Dict[str, object]:
    seq_matcher = difflib.SequenceMatcher(None, s1, s2)
    matches = []
    for tag, i1, j1, i2, j2 in seq_matcher.get_opcodes():
        if tag == 'equal':
            match_dict: Dict[str, object] = {
                "type": "match",
                "start_s1": i1,
                "end_s1": j1,
                "start_s2": i2,
                "end_s2": j2,
                "content": s1[i1:j1],
            }
        elif tag == 'replace':
            match_dict: Dict[str, object] = {
                "type": "replacement",
                "start_s1": i1,
                "end_s1": j1,
                "start_s2": i2,
                "end_s2": j2,
                "content_before_replace": s1[i1:j1],
                "content_after_replace": s2[i2:j2],
            }
        elif tag == 'delete':
            match_dict: Dict[str, object] = {
                "type": "deletion",
                "start_s1": i1,
                "end_s1": j1,
                "content_deleted": s1[i1:j1],
            }
        elif tag == 'insert':
            match_dict: Dict[str, object] = {
                "type": "insertion",
                "start_s2": i2,
                "end_s2": j2,
                "content_inserted": s2[i2:j2],
            }
        matches.append(match_dict)
    similarity_ratio: float = seq_matcher.ratio()
    return {
        "similarity_score": round(similarity_ratio, 4),
        "operations": matches,
        "string_1_length": len(s1),
        "string_2_length": len(s2),
    }
if __name__ == '__main__':
    sample_string_a = "The quick brown fox jumps over the lazy dog"
    sample_string_b = "The quick brown fox jumped over the lazy dog."
    result: Dict[str, object] = compare_strings_high_performance(sample_string_a, sample_string_b)
    import json
    print(json.dumps(result))