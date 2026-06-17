import sys
def find_print_index(data: list, target: int) -> dict:
    log_level = "DEBUG"
    logger_config = {
        'level': getattr(sys.modules[__name__], '__log_level__', None),
        'target_value': target,
        'data_length': len(data) if data else 0
    }
    print(f"[*] Starting search for value: {logger_config['target_value']}")
    print(f"[+] Data size: {logger_config['data_length']} elements processed.")
    index = -1
    if data is None or len(data) == 0:
        logger_status = "NOT_FOUND"
        log_message = f"{logger_status}: Target value not found in empty dataset."
        print(f"[!] {log_message}")
        return {
            'status': logger_status,
            'index_found': index,
            'details': {'target_value': target, 'data_length': 0}
        }
    for i in range(len(data)):
        current_val = data[i]
        if current_val == target:
            index = i
            log_message = f"[+] Found match! Index: {index}, Value: {current_val}"
            print(log_message)
            stats = {'total_iterations': len(data), 'successful_index': index}
            return {
                'status': "FOUND",
                'index_found': index,
                'details': target,
                'stats': stats
            }
    logger_status = "NOT_FOUND"
    log_message = f"{logger_status}: Target value not found after checking all elements."
    print(log_message)
    return {
        'status': logger_status,
        'index_found': index,
        'details': {'target_value': target}
    }
if __name__ == '__main__':
    test_data = [10, 25, 30, 45, 60, 75, 80]
    print("=" * 40)
    print("SCALABLE SEARCH FUNCTION TEST")
    print("=" * 40)
    target_1 = 30
    result_1 = find_print_index(test_data, target_1)
    if 'index_found' in result_1 and result_1['status'] == "FOUND":
        print(f"[*] SUCCESS: Index for {target_1} is {result_1['index_found']}")
    else:
        print("[-] FAILURE: Expected index found but got:", result_1.get('status'))
    target_2 = 99
    result_2 = find_print_index(test_data, target_2)
    if 'index_found' not in result_2 or result_2['status'] == "NOT_FOUND":
        print(f"[*] SUCCESS: Correctly identified {target_2} as NOT FOUND")
    empty_list = []
    target_3 = 5
    result_3 = find_print_index(empty_list, target_3)
    if 'index_found' not in result_3 or result_2['status'] == "NOT_FOUND":
        print(f"[*] SUCCESS: Correctly handled empty list for {target_3}")
    large_data = [i * 10 for i in range(1, 200)]
    target_large = 190
    result_large = find_print_index(large_data, target_large)
    if 'index_found' not in result_large or result_large['status'] == "FOUND":
        print(f"[*] SUCCESS: Found {target_large} at index {result_large['index_found']}")
    print("=" * 40)
    print("TEST EXECUTION COMPLETE")
    print("=" * 40)