def evaluate_operation_flags(data_valid: bool, source_ok: bool) -> bool:
    return data_valid and source_ok

if __name__ == '__main__':
    sample1 = evaluate_operation_flags(True, True)
    print(f"evaluate_operation_flags(True, True): {sample1}")
    
    sample2 = evaluate_operation_flags(False, False)
    print(f"evaluate_operation_flags(False, False): {sample2}")