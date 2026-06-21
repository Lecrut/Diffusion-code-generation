class ChecklistMapper:
    def __init__(self):
        self.membership_status = {
            'item1': 'Member',
            'item2': 'Non-Member',
            'item3': 'Pending'
        }

    def map_items(self, checklist: dict) -> dict:
        return {item: self.membership_status.get(item, 'Unknown') for item in checklist}

if __name__ == '__main__':
    mapper = ChecklistMapper()
    sample_checklist = {'item1', 'item4'}
    result = mapper.map_items(sample_checklist)
    print(result)