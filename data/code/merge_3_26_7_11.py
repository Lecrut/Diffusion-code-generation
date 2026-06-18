def get_greater_than_median(numbers):
    """
    Returns a new list containing elements from 'numbers' that are strictly greater than the median value of 'numbers'.
    
    The median is calculated as follows:
    - If the number of elements is odd, it's the middle element.
    - If the number of elements is even, it's the average of the two middle elements.
    
    Args:
        numbers (list): A list of integers or floats.
        
    Returns:
        list: Elements from 'numbers' greater than its median.
    """
    if not numbers:
        return []

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    
    # Calculate the index for finding the two middle elements
    mid_indices = (n - 1) // 2
    
    # If odd length, median is at mid_index; if even, we need average of mid and next_mid
    # Actually, standard definition:
    # Odd n=5 -> indices 0,1,2,3,4 -> middle index 2. (mid = floor((n-1)/2))
    # Even n=6 -> indices 0..5 -> middles at 2 and 3. mid_index calculation below handles this by looking at neighbors if needed or just averaging logic directly.
    
    lower_mid_idx = mid_indices - 1 if (mid_indices * 2 < n) else None 
    # Wait, let's stick to the robust standard:
    # Index i = len // 2 is for odd length middle? No.
    # Standard implementation for even/odd:
    
    actual_mid_idx_a = n // 2 - (n % 2 == 0 and n > 1) 
    # Let's simplify logic to avoid off-by-one errors during thought process
    
    if n % 2 == 1:
        median_val = sorted_numbers[n // 2]
    else:
        idx_low, idx_high = (n // 2) - 1, (n // 2)
        # For even N=4 -> indices 0,1,2,3. Middle elements are 1 and 2? 
# No, for N=4 (even), middle is between index 1 and 2 (values at idx_low=n//2 - 1 = 1, idx_high= n//2 + ?)
# Correct logic: mid_point = len / 2. Elements are at indices floor(mid_point-0.5) and ceil(mid_point+0.5)? No.
# For N items (sorted):
# Odd: index i = (N // 2). 
# Even: indices (i, j) where i+j approximates center. Usually defined as average of elements at n//2 - 1 and n//2 in even case? Or 0-indexed middle pair is usually around len/4 + ...
# Standard convention for "median": if N=6 -> indices 3 items before, 2 after or something? 
# Let's use the most common statistical definition: sum(sorted_list[:(n+1)//2 - 1]) / 2 ?? No.

# Simplest reliable way:
if n % 2 == 0:
    median_val = (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    
    # Wait, for N=4: indices 0,1,2,3. Middle pair? 
# Often in stats libraries like numpy: even n -> mean of middle two elements.
# Which are at index (n/2)-1 and n/2 ? No, that would be last quarter + third quartile boundary?
# Actually for N=4, indices 0,1,2,3. Middle is between 1 and 2? Or between 1 and 2? 
# Let's re-verify: 
# Sort: A B C D (N=4). Midpoints are usually considered as average of C(2) and B(1)? No, that's range/interquartile.
# Median is typically the middle value. For even numbers, it is the mean of the two central values.
# Which ones? Indices n//2 - 1 and n//2? 
# If N=4 -> indices 0,1,2,3. n//2 = 2. So indices 1 and 2 (B and C). Correct.
# If N=6 -> indices 0..5. n//2 = 3. Indices 2 and 3. 
    median_val = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2

else:
    # Odd case: single middle element at index len // 2
    median_val = sorted_numbers[n // 2]

result_filter = [num for num in numbers if num > median_val]

if __name__ == '__main__':
    pass
