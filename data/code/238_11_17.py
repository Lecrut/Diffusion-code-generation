def create_hollow_square(side_length):
    if side_length < 2:
        return ""
    
    def build_top_bottom_row(length):
        return "*" * length
    
    def build_middle_rows(length, count):
        middle_row = "*" + " " * (length - 2) + "*"
        return [middle_row] * (count - 2)
    
    if side_length == 2:
        return build_top_bottom_row(side_length)
    
    top_bottom = build_top_bottom_row(side_length)
    middle = build_middle_rows(side_length, side_length)
    
    return "\n".join(top_bottom + middle)

if __name__ == '__main__':
    sample_side_length = 4
    print(create_hollow_square(sample_side_length))