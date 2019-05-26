def test_another_repr():
    mock_db = self.create_mock_database()
    first_people = People("Ada", 31)
    second_people = People("Ada", 25)

    result = self.visit_two(first_people, second_people)
    # .....
