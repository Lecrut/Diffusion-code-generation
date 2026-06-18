import difflib
import json
def compare_strings_high_performance(s1: str, s2: str) -> dict:
    sequence_matcher = difflib.SequenceMatcher(None, s1, s2)
    matches = list(sequence_matcher.get_matching_blocks())
    report_data = {
        "string_1": s1,
        "string_2": s2,
        "total_length_s1": len(s1),
        "total_length_s2": len(s2),
        "match_count": len(matches),
        "matches": [],
        "overall_similarity_ratio": sequence_matcher.ratio()
    }
    for block in matches:
        match_data = {
            "start_index_1": block.a,
            "end_index_1": block.a + block.size,
            "start_index_2": block.b,
            "end_index_2": block.b + block.size,
            "matched_text": s1[block.a:block.a+block.size] if block.size > 0 else ""
        }
        report_data["matches"].append(match_data)
    return report_data
if __name__ == '__main__':
    sample_str_1 = "Hello World"
    sample_str_2 = "Hello WorlD"
    result = compare_strings_high_performance(sample_str_1, sample_str_2)
    print(json.dumps(result))