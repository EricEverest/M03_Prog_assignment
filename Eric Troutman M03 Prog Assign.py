things = ["mozzarella", "cinderella", "salmonella"] 
print(things)

for i in things:
    print(i.capitalize())
#Capitalization does not change list

for i in things:
    print(i.upper())

#Capitalization does not change list
    
things = things[:-1]
print(things)


#-----------------------------------


def good():
    return ['Harry', 'Ron', 'Hermione']

def get_odds():
    for num in range(1, 10, 2):
        yield num

count = 0
for odd_number in get_odds():
    count += 1
    if count == 3:
        print("Third odd number:", odd_number)
        break