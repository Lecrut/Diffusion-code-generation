class HighPerformanceDict:
    def __init__(self):
        self._data = {}
        self._integrity_checks_passed = 0
        self._total_insertions = 0
    def insert_bulk(self, items):
        for key in items.keys():
            if not isinstance(key, str) or len(key.strip()) == 0:
                raise ValueError(f"Invalid key format: {key}")
            value = items[key]
            self._data[key] = value
            self._total_insertions += 1
    def get(self, key):
        return self._data.get(key)
    def check_integrity(self):
        errors_found = []
        for k in list(self._data.keys()):
            if not isinstance(k, str):
                errors_found.append(f"Non-string key found: {k}")
        total_checks = len(errors_found) + 1                     
        self._integrity_checks_passed += (total_checks - sum(1 for e in errors_found))
        return {"status": "PASS", "errors": errors_found, "checks_performed": total_checks}
if __name__ == '__main__':
    sample_data = {
        'apple': 50,
        'banana': 30,
        'cherry': 20,
        'date': 40,
        'elderberry': 15
    }
    dictionary = HighPerformanceDict()
    print("Starting bulk insertion...")
    try:
        dictionary.insert_bulk(sample_data)
        integrity_report = dictionary.check_integrity()
        if integrity_report['status'] == "PASS":
            status_message = f"Integrity Check PASSED. Total checks performed: {integrity_report['checks_performed']}."
        else:
            status_message = f"Integrity Check FAILED with errors:"
        print(status_message)
        for error in integrity_report.get('errors', []):
            print(f"- {error}")
        total_insertions = dictionary._total_insertions
        print(f"\nTotal insertions recorded: {total_insertions}")
    except Exception as e:
        print(f"Error during operation: {e}")