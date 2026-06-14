def repeat_sequence(start, factor):
    sequence = []
    current = start
    while current <= start + factor * 100:
        sequence.append(str(current))
        current += 1
    output = ""
    for i in range(0, len(sequence), factor):
        output += " ".join(sequence[i:i + factor]) + "\n"
    print(output.strip())
if __name__ == '__main__':
    repeat_sequence(5, 3)