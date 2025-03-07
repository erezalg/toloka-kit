__all__ = [
    'InfiniteOverlapParametersMixin',
]
import typing


class InfiniteOverlapParametersMixin:
    """This mixin provides `overlap` and `infinite_overlap` attributes
    and is responsible for maintaining their consistency.

    Possible states:
    * `overlap` is None and `infinite_overlap` is None:
        Interpreted as "overlap was not provided"
    * `overlap` is None and `infinite_overlap` is True:
        Interpreted as "infinite overlap"
    * `overlap` is not None and `infinite_overlap` is False:
        Interpreted as "finite overlap of `overlap`"

    All other states are considered invalid
    """

    def __attrs_post_init__(self): ...

    def unset_overlap(self):
        """Unsets overlap
        """
        ...

    def unstructure(self) -> typing.Optional[dict]:
        """Ensures that if either overlap or infinite_overlap is not None, then
        both of them are present in unstructured value.
        """
        ...

    def __init__(
        self,
        infinite_overlap=None,
        overlap=None
    ) -> None:
        """Method generated by attrs for class InfiniteOverlapParametersMixin.
        """
        ...

    _infinite_overlap: typing.Optional[bool]
    _overlap: typing.Optional[int]
