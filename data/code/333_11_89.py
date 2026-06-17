class StringProcessor:
    def get_first_chars(self, text):
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""
        words = []
        current_word_start_index = None
        for i in range(len(text)):
            char = text[i]
            is_alpha_numeric_or_underscore = ('a' <= char.lower() <= 'z') or \
                                              ('0' <= char.upper() <= '9') or \
                                              char == '_'
            if not current_word_start_index:
                words.append(char)
                current_word_start_index = i
            elif is_alpha_numeric_or_underscore and text[i-1] != " ":
                continue
        return "".join(words)
if __name__ == '__main__':
    processor = StringProcessor()
    test_cases = [
        "Hello World",
        "Python Programming is Fun!",
        "",
        "   ",
        "a_b_c_d_e_f_g_h_i_j_k_l_m_n_o_p_q_r_s_t_u_v_w_x_y_z_1234567890"
    ]
    for test_input in test_cases:
        result = processor.get_first_chars(test_input)
        print(f'Input: "{test_input}" -> Output: "{result}"')