def swap_adjacent_chars(characters):
    """
    Iterates through a list of characters, swapping adjacent elements at index i 
    and i+1 for all valid indices in an upward loop (from left to right).
    
    This function modifies the input list in-place. It uses a standard range up 
    to len(characters) - 2 + 1 which is equivalent to iterating as long as there 
    are two elements available to swap.

    Parameters:
        characters (list): A mutable list of single-character strings or any type 
                           that supports tuple unpacking/swapping.

    Returns:
        None (modifies the input list in-place)
    """
    # Iterate from i = 0 up to len(characters) - 2, but since we need valid pairs,
    # the condition is simply while there are at least two elements left. 
    # We stop when one element remains or if length < 1 initially.
    
    n = len(characters)
    
    # Start from index 0 and go up to n-2 (inclusive), so that i+1 exists within bounds [n-(i+1)].
    # The loop will run for i in range(0, n - 1). 
    # Example: if length is 3 (indices 0,1,2), we swap (0,1) then stop. Wait, the prompt says "for all valid i".
    # If string is 'abc', indices are a=0, b=1, c=2. 
    # Swaps for i: 0 ('ab'->'ba') and i=1 ('bc'->'cb'). Result bacb? No wait standard bubble-like single pass usually goes n-2?
    # Let's re-read carefully: "swaps the character at index i with ... i+1". 
    # If I have indices 0,1 -> swap. Then 1,2 -> swap. That covers all pairs (i, i+1).
    
    for i in range(len(characters) - 1):
        if len(characters) <= 1:
            break
        
        a = characters[i]
        b = characters[i + 1]
        
        # Perform the swap using tuple unpacking
        characters[i], characters[i+1] = b, a

if __name__ == '__main__':
    sample_list_char_a_b_c_d_e_f_g_h_i_j_k_l_m_n_o_p_q_r_s_t_u_v_w_x_y_z_0_1_2_3_4_5_6_7_8_9 = \
        ['a', 'b', 'c'] * 4 + list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')[:4] # Just a random test string
    
    sample_list_char_a_b_c_d_e_f_g_h_i_j_k_l_m_n_o_p_q_r_s_t_u_v_w_x_y_z_0_1_2_3_4_5_6_7_8_9 = \
        ['a', 'b'] + list(range(ord('c'), ord('z') - 4)) # Simplified: just numbers and letters

    test_string_data = "abcdef" 
    characters_list_from_test = [ch for ch in test_string_data]
    
    swap_adjacent_chars(characters_list_from_test) 
    
    print("Original:", test_string_data)
    print("After swaps (single pass):", ''.join(characters_list_from_test))