class room:
    actions = [None,None,None,None]
    story = 'This is a generic room'
    visit_count = 0
    is_end = False

    def __init__(self, stories, exit_list, end_visit_count=-1):
        self.story = stories[0]
        self.stories = stories
        self.actions = exit_list
        self.end_visit_count = end_visit_count

    def update_visit(self):
        self.visit_count+=1
        if self.visit_count<len(self.stories):
            self.story = self.stories[self.visit_count]
        if self.end_visit_count>0 and self.end_visit_count<=self.visit_count:
            self.is_end=True

balcony_0 = room(['This is the balcony. There is a splendid view of mountains and a crystal clear lake. Wind blows through your hair and cotton top.',
                  'This is the balcony. As you admire the view again, you feel a sharp push from behind, and tumble into the lake. In the last few moments before you drown, you see a little girl smiling from the place you were pushed.'],[None,None,None,6],end_visit_count=1)
bathroom_1 = room(['This is the bathroom. There is a sink and a toilet to the right of the door. A bath-tub is opposite the sink and toilet.',
                   'This is the bathroom. There is a sink and a toilet to the right of the door. The bath-tub is wobbling, and you know it was not doing that before. A hand sticks out, and grabs you. You scream, and get sucked down the drain. You die.'],[2,None,None,None],end_visit_count=1)
bedroom_2 = room(['This is the bedroom. A cute little bed, with a doll tucked into its covers sits in the corner. All of a sudden, a dog jumps out from behind the bed and runs out the door.',
                  'This is the bedroom. A cute little bed, with a doll tucked into its covers sits in the corner.'],[None,6,None,1])
closet_3 = room(['This is the closet. A pink-and-blue coat hangs in the center, along with a couple cloaks. You trip over some stray boots on the floor, and put your hand in a spiderweb. No one has been here in a long time.'
                 'This is the closet. Like before, coats and cloaks hang, and there are '],[None,5,None,None])
dining_room_4 = room(['This is the dining_room. A beautifully carved table, showing the life cycle of a plant, (including it crumbling to peices) is pristine, and looks as if it was just bought.'],[None,None,None,7])
foyer_5 = room(['This is the foyer. You blink. The inside of what is believed to be a run-down house is nothing like what you '
                'have ever seen before. As you look around, looking for the supposed treasure that you camed here to find, you push '
                'open the door that is to the...  '],[6,8,3,None])
hall_6 = room(['This is the hall. Crude discriptions are carved into the wall, and you avirt your eyes when you see someone naked being killed slowly by a mysterious force.'],[0,9,2,5])
kitchen_7 = room(['This is the kitchen. There is a little girl standing in the corner facing the wall. As you enter the room, she slowly looks over her shoulder at you and '
                  'grins. \"I am in timeout!\" she says, and her grin grows wider.',
                  'This is the kitchen. The little girl has found a knife and appears to be carving something into the wall.',
                  'This is the kitchen. You are stabbed from behind while looking for the little girl. As you fall to the ground, clutching your side, the little girl '
                  'calmly watches as you start to gasp. She then raises the knife again and thrusts. You die on the kitchen floor.',
                  ],[4,None,9,None],end_visit_count=2)
music_room_8 = room(['This is the music room. There are millions of instruments here, all looking like they came out of a fairy tale.',
                     'This is the music room. Where there used to be millions of instruments, there is nothing. Well, except a piece of wood you reconize as coming from a viola. As you pick up the piece, befudled, something sparkly catches your eye. You go towards it, but a little girl gets there first. She snarles at you. \"You almost got it! I WILL KILL YOU!!\"',
                     'This is the music room. Scared, you look around for the little girl, but she is nowhere to be found. Again, something sparkly catches your eye, and entranced, you walk toward it. It is the treasure! You pick it up. Suddenly, your vision blurrs, and you are outside the house, with the treasure in your hands. Thank you for playing! Have a nice day!'],[9,None,5,None])
tv_room_9 = room(['This is the tv room.'],[None,7,6,8])

room_list = []

current_location = 5
room_list.append(balcony_0)
room_list.append(bathroom_1)
room_list.append(bedroom_2)
room_list.append(closet_3)
room_list.append(dining_room_4)
room_list.append(foyer_5)
room_list.append(hall_6)
room_list.append(kitchen_7)
room_list.append(music_room_8)
room_list.append(tv_room_9)

doors = ['north', 'east', 'west', 'south']

while 1:
    print(room_list[current_location].story)
    # print(current_location, room_list[current_location].visit_count)
    if room_list[current_location].is_end:
        break
    str = 'There is a door to the '
    for i in range(0,4):
        if room_list[current_location].actions[i] is not None:
            str = str + doors[i] + ', '
    print(str)
    print('Where should we go next? (n,e,w,s)[r,q]')
    sel = input()
    room_list[current_location].update_visit()
    if sel=='n':
        if room_list[current_location].actions[0] is None:
            print('You can not go that way')
        else:
            current_location = room_list[current_location].actions[0]
    if sel=='e':
        if room_list[current_location].actions[1] is None:
            print('You can not go that way')
        else:
            current_location = room_list[current_location].actions[1]
    if sel=='w':
        if room_list[current_location].actions[2] is None:
            print('You can not go that way')
        else:
            current_location = room_list[current_location].actions[2]
    if sel=='s':
        if room_list[current_location].actions[3] is None:
            print('You can not go that way')
        else:
            current_location = room_list[current_location].actions[3]
    if sel=='r':
        print('Restarting in the Foyer')
        current_location = 5
    if sel=='q':
        print('Exiting the game. You died I guess...')
        break

print('Thank you for playing. Have a nice day.')
