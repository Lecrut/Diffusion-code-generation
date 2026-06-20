def compare_lengths(seq1, seq2):
    it1 = iter(seq1)
    it2 = iter(seq2)
    while True:
        try:
            next(it1)
        except StopIteration:
            len1_done = True
            break
    else:
        len1_done = False
    
    while True:
        try:
            next(it2)
        except StopIteration:
            len2_done = True
            break
    else:
        len2_done = False
    
    if len1_done and len2_done:
        return "equal"
    elif len1_done:
        return "second longer"
    elif len2_done:
        return "first longer"
    else:
        return "both ongoing"

def compare_lengths_generator(seq1, seq2):
    it1 = iter(seq1)
    it2 = iter(seq2)
    
    try:
        next(it1)
    except StopIteration:
        len1_done = True
    else:
        len1_done = False
    
    try:
        next(it2)
    except StopIteration:
        len2_done = True
    else:
        len2_done = False
    
    if len1_done and len2_done:
        yield "equal"
    elif len1_done:
        yield "second longer"
    elif len2_done:
        yield "first longer"
    else:
        yield "both ongoing"

if __name__ == '__main__':
    for result in compare_lengths_generator([1, 2], [3, 4, 5]):
        print(result)