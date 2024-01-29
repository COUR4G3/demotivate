"""A simple script to print random demotivations."""

import click
import random
import sys

from importlib.metadata import version


try:
    __version__ = version("demotivate")
except ImportError:
    __version__ = "?.?.? (it's broken)"


demotivations = [
    "No.",
    "Have a panic attack. You've earned it.",
    "Life. What a fucking nighmare.",
    "I am capable of making good decisions. But I'm fucking amazing at bad ones.",
    "Try and try until you cannot succeed.",
    "Trying is the first step towards failure.",
    "He who laughs last didn't get the joke.",
    "The reward for good work is more work.",
    "Accept that you're just a product, not a gift.",
    "Not everything is a lesson. Sometimes you just fail.",
    "Hope is the first step ofm the road to disappointment.",
    "The light at the end of the tunnel has been turned off due to budget cuts.",
    "It could be that your purpose in life is to serve as a warning to others",
    "If you think you're too small to make a difference, you're right.",
    "Success is simply a matter of luck. Ask any failure.",
    "Hard work may not always result in success, but it will always result in more work.",
    "Dream big and dare to fail. Or just dream small and save yourself the trouble.",
    "You miss 100% of the shots you don't take. But you also miss 100% of the shots you do take, so what's the point?",
    "Success is just failure that hasn't happened yet.",
    "Don't worry about the consequences; just go ahead and make those impulsive decisions.",
    "Why be motivated when you can embrace the soothing mediocrity of indifference?",
    "Dreams are for those who can't handle reality.",
    "The best things in life are actually really expensive.",
    "Challenging yourself...is a good way to fail.",
    "Do not take life too seriously. You will never get out of it alive.",
    "Everything happens for a reason. Sometimes the reason is you're stupid and make bad decisions.",
    "Every dead body on Mt. Everest was once a highly motivated person.",
    "If life doesn't break you today, don't worry. It will try again tomorrow.",
    "A thousand-mile journey starts with one step. Then again, so does falling in a ditch and breaking your neck.",
    "If you never try anything new, you'll miss out on many of life's great disappointments",
    "Just because you are unique doesn't mean you are useful.",
    "Always remember that you are absolutely unique. Just like everyone else.",
    "Life is pain. Anyone who says otherwise is selling something.",
    "Your life can't fall apart if you never had it together.",
    "Go ahead and take risks - it gives the rest of us something to laugh at.",
    "There's always someone on Youtube that can do it better than you.",
    "You're naturally funny because your life is a joke.",
    "If you never believe in yourself, you'll never let yourself down.",
    "You can be replaced.",
    "Happiness is just sadness that hasn't happened yet.",
    "I can but I won't.",
    "Today will be a day like every other day.",
    "You don't have 'haters'. No one knows who you are.",
    "The universe doesn't give a shit about you.",
    "What doesn't kill you fucks you up mentally.",
    "You weren't born to just pay bills and die. You must suffer, a lot.",
    "The light at the end of the tunnel is a train.",
    "Every morning wake up and scream your dreams into a garbage can where they belong.",
    "Every day is another change to screw everything up again.",
    "Before you judge someone else, keep in mind that you're probably a piece of shit too.",
    "It's a beautiful day to shut the fuck up.",
    "A great place to put inspirational quotes is up your own ass.",
    "The reason you have to follow your dreams is because your dreams are trying to get away from you.",
    "It's not just Monday, your whole life sucks.",
    "Monday hates you too.",
    "Just give up.",
    "Be yourself. No one else wants to be you.",
    "Remember to anyways be yourself. Unless you stuck.",
    "Be the reason why a co-worker has a meltdown.",
    "It's a bad life, not a bad day.",
    "Those who doubt your ability probably havea valid reason.",
    "Pretty soon we'll all be dead.",
    "If you hate yuorself, remember that you are not alone, a lot of other people hate you too.",
    "Always believe that something wonderful will probably never happen.",
    "Try hard and don't wory if you fail because everyone expected that.",
    "I can but I won't.",
    "Disappointed but not surprised.",
    "If you can't laugh at yourself that's okay, because the rest of us can laugh at you instead.",
    "It probably could get worse.",
    "It's never too late to go back to bed.",
    "Keep panicking.",
    "Nobody is perfect, shoot for adequate.",
    "Why stand out when you can blend in.",
    "Maturity is the time of life when, if you had the time, you'd have the time of your life.",
]


@click.command("demotivate")
@click.version_option(__version__)
def cli():
    """A simple script to print random demotivations."""
    text = demotivate()
    click.echo(f'"{text}"')


def demotivate():
    """Get a demotivational quote."""
    return random.choice(demotivations)


def main():
    cli.main(sys.argv[1:], prog_name="demotivate")


if __name__ == "__main__":
    main()
