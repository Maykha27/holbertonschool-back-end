#!/usr/bin/python3

"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

from requests import get
from sys import argv as arg


if __name__ == "__main__":
    api_todos_dict = {'userId': arg}
    response = get('https://jsonplaceholder.typicode.com/todos',params=api_todos_dict)
    data = response.json()
    completed = 0
    total = 0
    tasks = []
    response2 = get('https://jsonplaceholder.typicode.com/users')
    data2 = response2.json()

    for i in data2:
        if i.get('id') == int(arg[1]):
            Employee = i.get('name')

    for i in data:
        if i.get('userId') == int(arg[1]):
            total += 1

            if i.get('completed') is True:
                completed += 1
                tasks.append(i.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(Employee, completed,
                                                          total))

    for i in tasks:
        print("\t {}".format(i))
