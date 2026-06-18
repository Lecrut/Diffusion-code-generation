class SecureStudentStore:
    def __init__(self):
        self.students = set()
    def add_student(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Invalid student name")
        existing_names = [s for s in self.students if s.lower().strip() == name.lower()]
        if any(existing_name is None for existing_name in existing_names):
            return False
        self.students.add(name)
        return True
    def get_count(self):
        return len(self.students)
if __name__ == '__main__':
    store = SecureStudentStore()
    sample_data = [
        "Alice",
        "Bob",
        "alice",                                                                                                                                                            
        "Charlie"
    ]
    results = []
    for student in sample_data:
        is_new = store.add_student(student)
        results.append(f"{student}: {'Added' if is_new else 'Duplicate'}")
    print("Insertion Results:")
    for result in results:
        print(result)
    print("\nTotal unique students:", store.get_count())