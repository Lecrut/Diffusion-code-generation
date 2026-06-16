def check_list_integrity(data):
    for seq in data:
        if len(seq) == 0 or len(set(seq)) <= 1:
            continue
        first_val = seq[0]
        for val in seq[1:]:
            if val != first_val:
                return False
    return True
if __name__ == '__main__':
    sample_data = [
        [1, 2],                                      
        [3, 3],                   
        [],                                        
        [5]                                  
    ]
    result = check_list_integrity(sample_data)
    if result:
        print("All sub-sequences have equal values.")
    else:
        print("Some sub-sequences do not have equal values.")