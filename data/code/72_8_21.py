def compare_indices(data, indices):
    if not isinstance(data, (list, tuple)):
        raise TypeError("Data must be a list or tuple")
    if not isinstance(indices, (list, tuple)):
        raise TypeError("Indices must be a list or tuple")
    
    results = []
    n = len(data)
    m = len(indices)
    
    if m < 2:
        return results
        
    for k in range(m - 1):
        i1 = indices[k]
        i2 = indices[k + 1]
        
        if not isinstance(i1, int) or not isinstance(i2, int):
            raise TypeError("Indices must be integers")
            
        if i1 < 0 or i1 >= n:
            raise ValueError(f"Index {i1} out of range for data of length {n}")
        if i2 < 0 or i2 >= n:
            raise ValueError(f"Index {i2} out of range for data of length {n}")
            
        val1 = data[i1]
        val2 = data[i2]
        
        if val1 < val2:
            results.append(f"{val1} < {val2}")
        elif val1 > val2:
            results.append(f"{val1} > {val2}")
        else:
            results.append(f"{val1} == {val2}")
            
    return results

if __name__ == '__main__':
    sample_data = [10, 20, 15, 30, 25]
    sample_indices = [0, 2, 4, 1]
    output = compare_indices(sample_data, sample_indices)
    print(output)