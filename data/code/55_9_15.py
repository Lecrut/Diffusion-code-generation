def get_mirrored_char_sequence(index):
    base = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if index >= len(base):
        index = index % len(base)
    prefix = base[:index + 1]
    suffix = prefix[:-1][::-1]
    return prefix + suffix

def build_triangle_pattern(count):
    if count < 1:
        return ''
    lines = []
    for k in range(count):
        seq = get_mirrored_char_sequence(k)
        lines.append(seq)
    return '\n'.join(lines)

class PatternGenerator:
    def __init__(self, max_rows):
        self.max_rows = max_rows
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def generate_line(self, row_index):
        if row_index < 0:
            row_index = 0
        if row_index >= len(self.alphabet):
            row_index = len(self.alphabet) - 1
        head = self.alphabet[:row_index + 1]
        tail = head[:-1][::-1]
        return head + tail

    def render_full(self):
        result = []
        for r in range(self.max_rows):
            result.append(self.generate_line(r))
        return '\n'.join(result)

if __name__ == '__main__':
    sample_height = 7
    generator = PatternGenerator(sample_height)
    final_output = generator.render_full()
    print(final_output)