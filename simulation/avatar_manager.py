from simulation.avatar import AvatarRunner
from simulation.location import Location


class AvatarManager(object):
    def __init__(self, initial_avatars):
        self.avatarsById = {p.player_id: p for p in initial_avatars}

    def player_changed_code(self, player_id, code):
        avatar = self.avatarsById.get(player_id)
        if avatar is None:
            avatar = AvatarRunner(Location(0, 0), code, player_id)
            self.avatarsById[player_id] = avatar
        avatar.set_code(code)

    @property
    def avatars(self):
        return self.avatarsById.viewvalues()