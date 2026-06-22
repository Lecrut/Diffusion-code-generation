def compare_elements(list1, list2, index):
    status_codes = {
        "valid": "success",
        "missing": "index_out_of_bounds"
    }
    
    result = {}
    
    try:
        val1 = list1[index]
        result["list1"] = val1
        result["status1"] = status_codes["valid"]
    except IndexError:
        result["list1"] = None
        result["status1"] = status_codes["missing"]
        
    try:
        val2 = list2[index]
        result["list2"] = val2
        result["status2"] = status_codes["valid"]
    except IndexError:
        result["list2"] = None
        result["status2"] = status_codes["missing"]
        
    return result

if __name__ == '__main__':
    data_a = [100, 200, 300]
    data_b = [101, 201, 301]
    target_idx = 1
    output = compare_elements(data_a, data_b, target_idx)
    print(output)