"""An example of how to represent a group of acquaintances in Python."""
#A function taking in the data for one person and ammending the inputted dictionary with a nested dictionary containing thier data.
def add_to_group(Group,Name,Age,Job="",Connections={}): #Connections is a list of 2 element tuples
    Group[Name] = {"age": Age, "job": Job, "connections":{Relationship[0]:Relationship[1] for Relationship in Connections}}
    return None

#Implimenting instances of a group network using the 'add_to_group' function for the provided data.
my_group = {}
add_to_group(my_group,"Jill",26,"Biologist",Connections=[("Friend","Zalika"),("Partner","John")])
add_to_group(my_group, "Zalika",28,"Artist",Connections=[("Friend","Jill")])
add_to_group(my_group, "John",27,"Writer", Connections=[("Partner", "Jill")])
add_to_group(my_group, "Nash",34,"Chef",Connections=[("Cousin","John"),("Landlord","Zalika")])

print(my_group)


#add some code that makes use of comprehension expressions to your group.py file so that it prints out the following script when run

#max age of people in the group
#average number of relationships of the group
#max age of the people in the group with at least one relation
#the maximum age of the people iin the group with at least one FRIEND

#for Name in my_group:
    #print(my_group[Name]["age"])

#Max age of people in the group:

max_age = max([my_group[Name]["age"] for Name in my_group])
print("The maximum age of this group is: ", max_age)

#Average number of relationships of the group

n_o_people = len(my_group.keys())
n_o_conns = [len(my_group[Names]["connections"].keys()) for Names in my_group]
average_conn = sum(n_o_conns)/n_o_people
print("The average number of connections in this group is: ", average_conn)

#Max age of the people in the group with at least one relation

#OUTPUTS THE MAX CONNECTIONS i.e. 2 NOT THE AGE OF THAT PERSON AT THE MOMENT
at_least_one_R = [number for number in n_o_conns if number >=1]
max_age_R = max(at_least_one_R)
print("The maximum age of people in this group with at least one relationship is: ", max_age_R)

