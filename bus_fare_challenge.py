import bus_fare_challenge as solution
import datetime
import unittest


class TestBusFareChallenge(unittest.TestCase):
    def setUp(self) -> None:
        self.date = datetime.datetime.now().date()
        self.day = self.date.strftime("%a")
        self.charts = {
            "Mon": 150,
            "Tue": 150,
            "Wed": 150,
            "Thu": 150,
            "Fri": 100,
            "Sat": 50,
            "Sun": 120,
        }

    def test_date(self) -> None:
        actual = self.date
        given = solution.date
        self.assertEqual(actual, given, f"Today's date is Wrong by {given - actual}!")

    def test_day(self) -> None:
        actual = self.day
        given = solution.day
        self.assertEqual(
            actual, given, f"Today is wrong, expexted {actual} but got {given}!"
        )

    def test_fare(self) -> None:
        actual = self.charts[self.day]
        given = solution.fare
        self.assertEqual(
            actual, given, f"Fare is wrong, expected {actual} but got {given}!"
        )


if __name__ == "__main__":
    
    print("Tracking___: Checking Values For Today's  Date, Day and Fare =====")
    unittest.main(exit=False)
    print("EndTracking___: Checking Return Values For Today's  Date, Day and Fare =======")
