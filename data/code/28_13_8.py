def compress_rle(source):
    if not source:
        return ""
    builder = []
    head = source[0]
    tally = 1
    for char in source[1:]:
        if char == head:
            tally += 1
        else:
            builder.append(str(tally))
            builder.append(head)
            head = char
            tally = 1
    builder.append(str(tally))
    builder.append(head)
    return "".join(builder)

if __name__ == '__main__':
    sample_data = "AAAAABBBBCCCCDDDDDDDDEEEEEEEEEEEFFFFFGGGGGGGGGGGHHHHHHHHHHHIIIIIIIIIIJJJJJJJJJJKKKKKKKKKKLLLLLLLLLLMMMMMMMMMMNNNNNNNNNNOOOOOOOOOPPPPPPPPPPQQQQQQQQQQRRRRRRRRRRSTTTTTTTTTTUUUUUUUUUUWWWWWWWWWWXXXYYYYYYYZZZZZZZZZ"
    output = compress_rle(sample_data)
    print(output)