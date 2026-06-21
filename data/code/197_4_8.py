def map_checklist_items(checklist: dict) -> dict:
    status_mapping = {
        'pending': 'Not Started',
        'in_progress': 'In Progress',
        'completed': 'Completed'
    }
    return {item: status_mapping.get(status, 'Unknown') for item, status in checklist.items()}

if __name__ == '__main__':
    sample_checklist = {
        'Task 1': 'pending',
        'Task 2': 'in_progress',
        'Task 3': 'completed',
        'Task 4': 'unknown'
    }
    print(map_checklist_items(sample_checklist))