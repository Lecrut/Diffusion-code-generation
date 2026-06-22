def combine_checks(is_positive, is_even, is_less_than_100):
    status_labels = {
        True: "positive",
        False: "not positive"
    }
    parity_labels = {
        True: "even",
        False: "odd"
    }
    range_labels = {
        True: "less than 100",
        False: "greater than or equal to 100"
    }
    
    parts = []
    
    if is_positive:
        parts.append(status_labels[True])
    else:
        parts.append(status_labels[False])
        
    if is_even:
        parts.append(parity_labels[True])
    else:
        parts.append(parity_labels[False])
        
    if is_less_than_100:
        parts.append(range_labels[True])
    else:
        parts.append(range_labels[False])
        
    return " | ".join(parts)

if __name__ == '__main__':
    result = combine_checks(False, True, False)
    print(result)