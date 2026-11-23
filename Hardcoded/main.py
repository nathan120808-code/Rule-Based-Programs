import pandas as pd


#RULES - all are built on reasoning with the existing variables on the dataset
#format: ({condition}, conclusion)

PRICE_RULES = [
    ({"price" : {"vhigh"}, "maint": {"vhigh"}}, "price_high"),
    ({"price": {"low","med"}, "maint": {"low","med"}}, "price_low")
]
PRICE_DEF = "price_med"

COMFORT_RULES=[
    ({"persons":{2}, "boot": {"small"}}, "comfort_low"),
    ({"persons":{"more"}, "boot": {"high"}}, "comfort_high")
]
COMFORT_DEF = "comfort_med"

TECH_RULES = [
    ({"safety": {"low"}, "comfort": {"comfort_low"}}, "tech_low"),
    ({"safety": {"high"}, "comfort": {"comfort_med", "comfort_high"}}, "comfort_high")
]
TECH_DEF = "tech_med"

CLASS_RULES = [
    ({"tech":{"tech_low"}}, "unacc"),
    ({"comfort":{"comfort_low"}}, "unacc"),
    ({"price":{"price_high"}}, "unacc"),
    ({"tech": {"tech_high"}, "price": {"price_low"}, "comfort":{"comfort_high"}}, "vgood")
    ({"tech": {"tech_high"}, "comfort":{"comfort_high"}}, "good")
]
CLASS_DEF = "acc"

def deploy_rule(facts,rules,default):
    """this function goes through all the rules and references it against the inputted car's known facts - the moment it finds a matching criteria the rule fires, returning true, if not it goes back to the default values returning false"""
    for condition, conclusion in rules:
        if all(facts.get(attr) in allowed for attr, allowed in condition.items()):
            return conclusion, True
    return default, False