# To do list application
# Add 
# update 
# delete 
# Exit
# Save it 
# todo_list = []
# while True: 
#     todo = input("press 1 to add and 2 to delete?")
#     if todo == "Exit":
#         break
#     todo_list.append (todo)
# print (todo_list)


# todo_list = []
# while True: 
#     todo = int(input("press 1 to add, 2 to delete, 3 to update, 4 to exit?"))
#     if todo == 4:
#         break
#     if todo == 1:
#        todo_1 = input("What will you like to add?")
#        todo_list.append(todo_1)
#     if todo == 2:
#        todo_2 = input("What will you like to detele?")
#        todo_list.remove(todo_2)
#     if todo == 3:
#        todo_3 = input("What will you like to update?")
#        target_index = todo_list.index (todo_3)
#        todo_4 = input("What will you like to update to?")
#        todo_list[target_index] = todo_4
# print (todo_list)

# todo_list = {}
# while True: 
#     todo = int(input("press 1 to add, 2 to delete, 3 to update, 4 to exit?"))
#     if todo == 4:
#         break
#     if todo == 1:
#        todo_1 = input("What will you like to add?")
#        todo_list[len(todo_list)+1] = todo_1 
#     if todo == 2:
#        todo_2 = input("What will you like to detele?")
#        for key, value in todo_list.items():
#           if value == todo_2:
#             target_index = key
#        todo_list.pop(target_index)
#     if todo == 3:
#        todo_3 = input("What will you like to update?")
#        for key, value in todo_list.items():
#           if value == todo_3:
#             target_index = key
#        todo_4 = input("What will you like to update to?")
#        todo_list[target_index] = todo_4
# print (todo_list)

person = {
   "first_name": "Sola",
   "last_name": "Enitilo"
   
}
person ["height"] = 1.81
person.pop('height')
print(person)