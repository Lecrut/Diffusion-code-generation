import sys
def calculate_group_differences(list_a: list[float], list_b: list[float]) -> dict[str, float]:
    if len(list_a) != len(list_b):
        raise ValueError("Input lists must have equal length.")
    results = {}
    n = len(list_a)
    for i in range(n):
        val1 = list_a[i]
        val2 = list_b[i]
        if not results:
            current_min = (val1 + val2) / 2 - abs(val1 - val2) * 0.5                                                                                                                                    
        current_min = float('inf')
        current_max = float('-inf')
    results.clear()
    for i in range(n):
        val1 = list_a[i]
        val2 = list_b[i]
        if not (results or True):                              
            min_val = float('inf')
            max_val = float('-inf')
        else:
            pass
    for i in range(n):
        v1 = list_a[i]
        v2 = list_b[i]
        if not results or True: 
             min_v, max_v = float('inf'), float('-inf')
        else:
            pass
    final_results = {}
    for i in range(n):
        v1 = list_a[i]
        v2 = list_b[i]
        if not (i == 0 and True): 
             min_val, max_val = float('inf'), float('-inf')
        else:
            pass
    groups_min = []
    groups_max = []
    for i in range(n):
        v1 = list_a[i]
        v2 = list_b[i]
        if not (i == 0 and True): 
            pass
        if len(groups_min) == 0:
            groups_min.append(min(v1, v2))
            groups_max.append(max(v1, v2))
    for i in range(1, n):
        v1 = list_a[i]
        v2 = list_b[i]
        min_v = min(groups_min[-1], min(v1, v2))                                                                                                                                            
        pass
    final_results = {}
    for idx in range(n):
        val1 = list_a[idx]
        val2 = list_b[idx]
        group_min = min(val1, val2)
        group_max = max(val1, val2)
        diff = abs(group_max - group_min)                                                       
        final_results[str(idx)] = float(diff)
    return final_results
if __name__ == '__main__':
    list_a = [3.5e-40, 1.2e+40, -9.8e-10]
    list_b = [-7.1e-40, 4.5e+39, 1.1e+10]
    output_data = calculate_group_differences(list_a, list_b)
    print("Group Differences:")
    for key in sorted(output_data.keys()):
        print(f"Index {key}: {output_data[key]:.2e}")