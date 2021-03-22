from datetime import datetime, timedelta
import time

class Insert:
    def __init__(self):
        self.quest = ""
        self.quest_time = 0
        self.quest_dict = {}
        # self.quest_time_dict = {}
        self.quest_time_dict = []
        self.rules = {}
        self.x = 0
        self.quest_counter = 0



    def inserting(self):
        while self.x != 1:

            self.quest = input("Please enter the quest you want to do today:")

            if self.quest in("end", "End"):
                if len(self.quest_dict) == 0:
                    print("There was an error please enter at least one quest")
                    exit()
                else:
                    print("Ended the whole process")
                    self.x += 1
                    System().manage(self)

            else:
                self.quest_time = int(input("Please enter the amount of hour(s) for your quest: "))
                print("added something to the dic")
                self.quest_dict[self.quest] = self.quest_counter
                # self.quest_time_dict[self.quest_time] = self.quest_counter
                self.quest_time_dict.append(self.quest_time)
                self.quest_counter += 1
                print(self.quest_counter)




class System:

    def __init__(self):
        self.one_hour = datetime.now() + timedelta(hours=1)
        self.two_hour = datetime.now() + timedelta(hours=2)
        self.three_hour = datetime.now() + timedelta(hours=3)
        self.four_hour = datetime.now() + timedelta(hours=4)
        self.updated_time = 0
        self.rule = {'1':f'{self.one_hour.strftime("%H")}', '2':f'{self.two_hour.strftime("%H")}', '3':f'{self.three_hour.strftime("%H")}', '4':f'{self.four_hour.strftime("%H")}'}





    def manage(self, instance):
        for i in instance.quest_time_dict:
            # hour = int(self.rule[str(i)]) - 12
            hour = int(self.rule[str(i)])



            if self.updated_time == 0:
                self.updated_time = i
            elif self.updated_time != 0:
                hour = hour + self.updated_time
                self.updated_time = self.updated_time + i


            if hour > 12:
                hour = hour - 12
                print("This is the hour", hour)


            if datetime.now().minute < 10:
                now = datetime.now()
                m = str(now.minute)
                m = "0" + m

                print(str(hour) + ":" + str(datetime.now().minute))

            else:

                print(str(hour)+":"+str(datetime.now().minute))








Insert().inserting()
