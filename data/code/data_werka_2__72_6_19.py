from typing import List, Tuple

RELATION_EQUAL = "equal"
RELATION_GREATER = "greater"
RELATION_LESS = "less"

def compare_pair_elements(first_list: List[int], second_list: List[int]) -> List[Tuple[int, int, str]]:
    results = []
    for val_a, val_b in zip(first_list, second_list):
        if val_a == val_b:
            relation = RELATION_EQUAL
        elif val_a > val_b:
            relation = RELATION_GREATER
        else:
            relation = RELATION_LESS
        results.append((val_a, val_b, relation))
    return results

def format_comparison_results(comparisons: List[Tuple[int, int, str]]) -> List[str]:
    formatted_lines = []
    for a, b, relation in comparisons:
        if relation == RELATION_EQUAL:
            formatted_lines.append(f"{a} == {b}")
        elif relation == RELATION_GREATER:
            formatted_lines.append(f"{a} > {b}")
        else:
            formatted_lines.append(f"{a} < {b}")
    return formatted_lines

if __name__ == '__main__':
    sample_a = [10, 20, 30, 40]
    sample_b = [10, 15, 35, 5]
    raw_comparisons = compare_pair_elements(sample_a, sample_b)
    display_lines = format_comparison_results(raw_comparisons)
    for line in display_lines:
        print(line)