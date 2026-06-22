def repeat_lines(input_file, output_file, Q):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                for _ in range(Q):
                    outfile.write(line)
        return f"Lines repeated {Q} times and written to {output_file}"
    except FileNotFoundError:
        return "Input file not found"
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    result = repeat_lines("sample.txt", "output.txt", 3)
    print(result)