import json
def store_student_names(names, filename):
    data = {"student_names": names}
    with open(filename, 'w') as f:
        json.dump(data, f)
if __name__ == '__main__':
    sample_names = [
        "Alice Smith",
        "Bob Johnson",
        "Charlie Brown",
        "Diana Prince"
    ]
    output_filename = "student_data.json"
    store_student_names(sample_names, output_filename)
    print(f"Data stored successfully in {output_filename}")