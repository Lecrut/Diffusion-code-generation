class RunLengthEncoder:
    def __init__(self, input_str):
        self.input_str = input_str
        self.runs = []
        self._compute_runs()

    def _compute_runs(self):
        if not self.input_str:
            self.runs = []
            return
        char_map = {}
        current_char = self.input_str[0]
        count = 1
        order_of_appearance = [current_char]
        for char in self.input_str[1:]:
            if char == current_char:
                count += 1
            else:
                char_map[current_char] = char_map.get(current_char, 0) + count
                current_char = char
                count = 1
        char_map[current_char] = char_map.get(current_char, 0) + count
        self.runs = [(char, char_map[char]) for char in order_of_appearance if char_map[char] == count and char == current_char]
        final_run = (current_char, count)
        if not self.runs or self.runs[-1][0] != current_char:
            self.runs.append(final_run)
        else:
            self.runs[-1] = (current_char, self.runs[-1][1] + count)

    def get_encoded_list(self):
        return self.runs

    def get_total_runs(self):
        return len(self.runs)

if __name__ == '__main__':
    encoder = RunLengthEncoder('aabbaaccc')
    print(encoder.get_encoded_list())
    print(encoder.get_total_runs())