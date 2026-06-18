import sys
def find_print_index(data_list: list, target_value) -> int:
    log_level = "DEBUG" if len(sys.argv) > 1 and sys.argv[1] == "--verbose" else "INFO"
    try:
        for idx, item in enumerate(data_list):
            print(f"[LOG {log_level}] Scanning index {idx}: value={item}")
            if item == target_value:
                return idx
        raise ValueError("Target not found")
    except Exception as e:
        print(f"[ERROR] Unexpected exception at line 15: {e}", file=sys.stderr)
        sys.exit(2)
if __name__ == '__main__':
    SAMPLE_DATA = [3, 7, 9, 4, 8, 6]
    TARGET_VALUE = 8
    try:
        result_index = find_print_index(SAMPLE_DATA, TARGET_VALUE)
        if result_index is not None:
            print(f"[SUCCESS] Target {TARGET_VALUE} found at index {result_index}")
        else:
            print("[FAILURE] Search completed without finding target")
    except ValueError as ve:
        print(f"[CRITICAL] {ve}", file=sys.stderr)