import random
when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 1st Jan', 'Once upon a time', 'Before man walked the earth']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle','a cat', 'a chicken', 'a butterfly', 'an ant']
name = ['Natasha', 'Ben', 'Casandra', 'Emily', 'Sam', 'George', 'Carmel']
residence = ['Spain','Russia', 'Germany', 'Venice', 'England', 'Ireland', 'Scotland', 'Wales', 'France', 'Italy', 'Austria']
went = ['cinema', 'laundry', 'party', 'mountains', 'lake', 'funfare', 'circus', 'zoo']
happened = ['made a lot of friends','Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']

print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened) + '.')
