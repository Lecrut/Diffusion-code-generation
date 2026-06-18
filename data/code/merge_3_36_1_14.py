def reverse_string(text: str) -> str:
    """Returns a new string with characters in 'text' reversed using slicing."""
    return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for demonstration; no user input required.
    samples = [
        "Hello, World!",
        "",
        "Python 3.9",
        "Race car example"
    ]

    results = []
    for item in samples:
        reversed_item = reverse_string(item)
        results.append(reversed_item)

    # Output each result on a new line to verify functionality without external I/O interaction.
    output_str = "\n".join(results)
    print(output_str if output_str else "No characters provided.")