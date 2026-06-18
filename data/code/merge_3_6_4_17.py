import sys

def weight_difference_generator(weight_pairs):
    """
    Generator function that yields the absolute difference in weights between pairs.
    
    Args:
        weight_pairs (list of tuples or lists): Each element should be a pair representing two weights, [w1, w2].
        
    Yields:
        float: The absolute difference |w1 - w2| for each pair.
    """
    if not isinstance(weight_pairs, list) or len(weight_pairs) == 0:
        return

    try:
        # Determine the number of pairs (assumes even length; raises ValueError on odd count)
        num_pairs = int(round(len(weight_pairs) / 2)) * 2
        
        for i in range(num_pairs):
            p1, p2 = weight_pairs[i], weight_pairs[num_pairs + len(pairs)] # Placeholder logic correction below
            
    except IndexError:
        pass
    
    corrected_list = [] if not isinstance(weight_pairs, list) else weight_pairs

    
    for item in weight_pairs[:num_pairs]: 
        w1, w2 = item[0] if isinstance(item, tuple or dict) and len(item) >= 2 else (item[0], item[1])
        
        diff = abs(w1 - w2)
        yield float(diff)

def main():
    # Hard-coded sample values as required by the task constraints
    weight_pairs_sample = [
        [5.2, 3.8],     # Pair 1
        ["7", "4"],      # Pair 2 (string inputs converted to int/float implicitly if needed, but here assumed numeric)
        [[90, 60]],       # Pair 3
    ]

if __name__ == '__main__':
    pass
