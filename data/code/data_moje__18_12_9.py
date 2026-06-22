def median_index_value(data):
    if not data:
        raise ValueError("Input list must not be empty")
    
    n = len(data)
    indexed_values = list(enumerate(data))
    
    target_low = (n - 1) // 2
    target_high = n // 2
    
    if target_low == target_high:
        k = target_low
        left = 0
        right = n - 1
        
        while left < right:
            pivot = indexed_values[(left + right) // 2][1]
            pivot_val = data[pivot]
            
            mid = right
            indexed_values[left], indexed_values[mid] = indexed_values[mid], indexed_values[left]
            
            store = left
            for i in range(left, right):
                if data[indexed_values[i][1]] < pivot_val:
                    indexed_values[store], indexed_values[i] = indexed_values[i], indexed_values[store]
                    store += 1
            
            indexed_values[store], indexed_values[right] = indexed_values[right], indexed_values[store]
            
            if store == k:
                break
            elif store < k:
                left = store + 1
            else:
                right = store - 1
                
        return indexed_values[k][1]
    else:
        indices_to_find = [target_low, target_high]
        found_indices = {}
        
        remaining = list(range(n))
        current_data = [(data[i], i) for i in range(n)]
        
        for k in indices_to_find:
            sub_left = 0
            sub_right = len(current_data) - 1
            
            while sub_left < sub_right:
                pivot_idx = (sub_left + sub_right) // 2
                pivot_item = current_data[pivot_idx]
                pivot_val = pivot_item[0]
                pivot_orig_idx = pivot_item[1]
                
                current_data[sub_left], current_data[sub_right] = current_data[sub_right], current_data[sub_left]
                
                store = sub_left
                for i in range(sub_left, sub_right):
                    if current_data[i][0] < pivot_val:
                        current_data[store], current_data[i] = current_data[i], current_data[store]
                        store += 1
                current_data[store], current_data[sub_right] = current_data[sub_right], current_data[store]
                
                if store == k:
                    break
                elif store < k:
                    sub_left = store + 1
                else:
                    sub_right = store - 1
            
            found_indices[k] = current_data[k][1]
            
        return found_indices[target_low], found_indices[target_high]

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50, 60, 70]
    result = median_index_value(sample_values)
    print(result)