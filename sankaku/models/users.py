from datetime import datetime

from pydantic import BaseModel, validator

from sankaku import types


__all__ = ["Profile", "ExtendedProfile"]


class Profile(BaseModel):
    """User profile model for any user that has an account on website."""

    last_logged_in_at: datetime
    favorite_count: int
    post_favorite_count: int
    vote_count: int
    post_vote_count: int
    pool_vote_count: int
    recommended_posts_for_user: int
    subscriptions: list[str]
    id: int
    name: str
    level: int
    upload_limit: int
    created_at: datetime
    favs_are_private: bool
    avatar_url: str
    avatar_rating: types.Rating
    post_upload_count: int
    pool_upload_count: int
    comment_count: int
    post_update_count: int
    note_update_count: int
    wiki_update_count: int
    forum_post_count: int
    pool_update_count: int
    series_update_count: int
    tag_update_count: int
    artist_update_count: int
    show_popup_version: int
    credits: int
    is_ai_beta: bool


class ExtendedProfile(Profile):
    """Profile of the currently logged-in user."""

    email: str
    hide_ads: bool
    subscription_level: int
    filter_content: bool
    receive_dmails: bool
    email_verification_status: str
    is_verified: bool
    verifications_count: int
    blacklist_is_hidden: bool
    blacklisted_tags: list[list[str] | str]
    blacklisted: list[str]
    mfa_method: int

    @validator("blacklisted_tags", pre=True)
    def flatten_blacklisted_tags(cls, v) -> list[str]:  # noqa
        return [tag[0] for tag in v]