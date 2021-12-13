class fbcontacts():

    def __init__(self,s,l,p,c,m,vc,v):

        self.__signup=s
        self.__login=l
        self.__profilesetup=p
        self.__contacts=c
        self.__messenger=m
        self.__videocall=vc
        self.__voicecall=v

    def display(self):

        self.type="private" or "public"
        print("private/public profile")

        self.friendslist="hide" or "show"
        print("hide/show friends list")

        self.addfriends="add the friends to your list"
        print("add friends")

        self.request="accept/reject friend request"
        print("accept/reject friend request")

        self.messages="reply" or "create message"
        print("type message/reply")

        self.post="create a new post"
        print("new post")

        self.hide="hide data from others "
        print("privacy")

        self.set="set your profile picture"
        print("set profile ")

        self.edit="edit your profile"
        print("edit profile")

        self.add="add from gallery" or "take photo"
        print("add profile picture")

    def promotions(self):

        self.invite="invite to facebook"
        print("invite others")

        self.suggestions="people you may know"
        print("suggestions for you")

        self.memory="collections of memory"
        print("a sweet memory")

    def safety(self):

        self.report="report unknown/fake id"
        print("report")

        self.block="block some messages" or" block account"
        print("block")

        self.password="create" or "change password"
        print("new password")

        self.link="link with gmail acc"
        print("link with gmail")

        self.notifications="hide" or "show"
        print("hide/show notifications")

        self.message="send messages to mobile"
        print("send notifications through message")



user=fbcontacts("signup","login","my profile","contacts you may know","messenger","videocall","voicecall")
user.display()
user.promotions()
user.safety()

if ("password doesnt match"):
    raise TypeError("invalid password ")
elif print("hi, welcome"):

    if ("forgot your password"):
        print("forgot password")


    
