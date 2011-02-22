import unittest
from datetime import datetime
from datetime import date
from twilio.rest import core


class CoreTest(unittest.TestCase):
    
    def test_date(self):
        d = date(2009,10,10)
        self.assertEquals(core.parse_date(d), "2009-10-10")

    def test_datetime(self):
        d = datetime(2009,10,10)
        self.assertEquals(core.parse_date(d), "2009-10-10")

    def test_string_date(self):
        d = "2009-10-10"
        self.assertEquals(core.parse_date(d), "2009-10-10")

    def test_string_date(self):
        d = None
        self.assertEquals(core.parse_date(d), None)

    def test_string_date(self):
        d = False
        self.assertEquals(core.parse_date(d), None)

    def test_fparam(self):
        d = {"HEY": None, "YOU": 3}
        ed = {"YOU":3}
        self.assertEquals(core.fparam(d), ed)

    def test_normalize_dates(self):

        @core.normalize_dates
        def foo(on=None, before=None, after=None):
            return {
                "on": on,
                "before": before,
                "after": after,
                }

        d = foo(on="2009-10-10", before=date(2009,10,10), 
                after=datetime(2009,10,10))

        self.assertEquals(d["on"], "2009-10-10")
        self.assertEquals(d["after"], "2009-10-10")
        self.assertEquals(d["before"], "2009-10-10")

    def test_convert_case(self):
        self.assertEquals(core.convert_case("from_"), "From")
        self.assertEquals(core.convert_case("to"), "To")
        self.assertEquals(core.convert_case("frienldy_name"), "FrienldyName")

    def test_convert_keys(self):
        d = {
            "from_": 0,
            "to": 0,
            "friendly_name": 0,
            "ended": 0,
            }

        ed = {
            "From": 0,
            "To": 0,
            "FriendlyName": 0,
            "EndTime": 0,
            }

        self.assertEquals(ed, core.convert_keys(d))
               