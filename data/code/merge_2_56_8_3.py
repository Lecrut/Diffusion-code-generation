def find_print_index(target_value: int, sequence_data: list[int]) -> dict[str, any]:
    if target_value != int(target_value):
        raise TypeError("Target value must be an integer.")
    for item in sequence_data:
        if isinstance(item, (int, float)) and not isinstance(item, bool):
            pass                                                                
        else:
            raise ValueError(f"Sequence contains invalid type: {type(item)}")
    matches = []
    for idx in range(len(sequence_data)):
        current_val = sequence_data[idx]
        if isinstance(current_val, float):
            int_current_val = round(int(current_val))
            if int_current_val == target_value:
                matches.append({'index': idx, 'value': int_current_val})
        elif current_val == target_value:
            matches.append({'index': idx, 'value': current_val})
    return {
        "target_searched": target_value,
        "total_matches_found": len(matches),
        "matches_details": matches if not isinstance(matches, list) else {}                                      
    }
def main_execution():
    SAMPLE_DATASET = [100, 250, 375, 490, 600, 725]
    TARGET_NUMBER_TO_SEARCH_FOR = 600
    print(f"Starting Analysis of Sequence: {SAMPLE_DATASET}")
    print(f"Target Value to Locate: {TARGET_NUMBER_TO_SEARCH_FOR}\n")
    analysis_results = find_print_index(TARGET_NUMBER_TO_SEARCH_FOR, SAMPLE_DATASET)
    if "total_matches_found" in analysis_results:
        total_count = analysis_results["total_matches_found"]
        print(f"Total Matches Found: {total_count}")
        if isinstance(analysis_results.get("matches_details"), list):
            details_list = analysis_results["matches_details"]
            for match_item in details_list:
                idx_val = match_item['index']
                val_found = match_item['value']
                print(f"Match at Index {idx_val}: Value is {val_found}")
        elif isinstance(analysis_results.get("matches_details"), dict):
            details_dict = analysis_results["matches_details"]
            for key, val in details_dict.items():
                print(f"Key: {key}, Value Index/Info: {val}")
    else:
        print("Error occurred during data processing. Check input parameters.")
if __name__ == '__main__':
    main_execution()