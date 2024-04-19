class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        method to set the default status variables of the tv
        :return: None
        """
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self) -> None:
        """
        method to turn the tv power on or off
        :return: None
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Method to mute the volume on the tv.
        :return: None
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Method to change the TV channel up by one. It does not
        go above the MAX_CHANNEL variable. Instead, if you are at max channel, it resets to min channel
        :return: None
        """
        if self.__status:
            if self.__channel < self.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Method to change the TV channel down by one. It does not go below the MIN_CHANNEL
        Variable. Instead, if you are at min channel, it jumps to max channel
        :return:
        """
        if self.__status:
            if self.__channel > self.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method that increases the volume by one. If you are at max_volume and the method is called,
        nothing happens.
        :return: None
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Method that decreases the volume by one. If you are at min_volume, and the method is called,
        nothing happens.
        :return:
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Method to show status of the TV.
        :return: tv status
        """
        if self.__muted:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = 0"
        else:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
