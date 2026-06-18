import json
def store_student_names(names):
    data = {"student_names": names}
    with open("student_data.json", "w") as f:
        json.dump(data, f)
if __name__ == '__main__':
    sample_names = [
        "Alice Smith",
        "Bob Johnson",
        "Charlie Brown",
        "Diana Prince",
        "Ethan Hunt"
    ]
    store_student_names(sample_names)
    print("Student names stored successfully in student_data.json")