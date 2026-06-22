def compare_elements(list_one, list_two, target_index):
    if target_index < 0:
        raise ValueError("Index must be non-negative")
    if not isinstance(list_one, list) or not isinstance(list_two, list):
        raise ValueError("Inputs must be lists")
    
    val_one = None
    val_two = None
    
    if target_index < len(list_one):
        val_one = list_one[target_index]
    
    if target_index < len(list_two):
        val_two = list_two[target_index]
        
    return val_one, val_two

def _generate_sample_data():
    data = {
        "first": [100, 200, 300, 400, 500],
        "second": [10, 20, 30, 40, 50, 60, 70],
        "indices": [1, 5, 10]
    }
    return data

if __name__ == '__main__':
    samples = _generate_sample_data()
    list_a = samples["first"]
    list_b = samples["second"]
    indices = samples["indices"]
    
    for idx in indices:
        res_a, res_b = compare_elements(list_a, list_b, idx)
        print(f"Index {idx}: {res_a}, {res_b}")