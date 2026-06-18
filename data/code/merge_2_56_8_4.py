def generate_sequence(start: int = 0, end: int = 100) -> list[int]:
    return list(range(start, end + 1))
def find_print_index(sequence: list[int], target_number: int) -> dict[str, any]:
    if not isinstance(sequence, list) or len(sequence) == 0:
        raise ValueError("Sequence must be a non-empty list.")
    if not isinstance(target_number, int):
        raise ValueError("Target number must be an integer.")
    indices = []
    for idx in range(len(sequence)):
        current_val = sequence[idx]
        if current_val == target_number:
            indices.append(idx)
    return {
        "found": len(indices) > 0,
        "index_list": indices,
        "count": len(indices),
        "target_searched": target_number
    }
def main() -> None:
    START_VALUE = 0
    END_VALUE = 50
    TARGET_NUMBER_TO_FIND = 27
    my_sequence: list[int] = generate_sequence(START_VALUE, END_VALUE)
    print(f"Sequence Generated (Length {len(my_sequence)}):")
    print("Sample elements:", my_sequence[:5], "...", my_sequence[-3:])
    result_data = find_print_index(sequence=my_sequence, target_number=TARGET_NUMBER_TO_FIND)
    if not result_data["found"]:
        print(f"Target {result_data['target_searched']} was NOT found in the sequence.")
    else:
        indices_found = result_data["index_list"]
        if len(indices_found) == 1:
            print(f"Target {result_data['target_searched']} is located at index: {indices_found[0]}")
        else:
            print(f"Target {result_data['target_searched']} appears multiple times.")
            for idx in indices_found:
                print(f"- Index found: {idx}")
if __name__ == '__main__':
    main()